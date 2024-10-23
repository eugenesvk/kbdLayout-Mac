#![allow(unused_imports,unused_variables,unreachable_code,dead_code,non_upper_case_globals)]
extern crate helper;
use helper            	::*; // gets macros
pub use helper_proc   	::*; // gets proc macros
pub use helper::alias 	::*;
pub use helper::helper	::*;

_mod!(binmod); //→ #[path="binmod/[binmod].rs"] pub mod binmod;
use crate::binmod::BpafAlias;

use anyhow::{Result,Context,bail};
use std::path::{Path, PathBuf}; // Path is a slice, PathBuf is like String owned, mutable
use std::str	::FromStr;

const FILE_IN : [&str;2] = ["../TypES Layout.bundle/Contents/Resources/English — TypES.keylayout","../TypES Layout.bundle/Contents/Resources/Russian — TypES.keylayout",];
const FILE_OUT: [&str;2] = ["../helper/SymbolsAll-En_Names.md","../helper/SymbolsAll-Ru_Names.md",];

#[allow(dead_code)] #[derive(Debug, Clone)]
struct OutCliArg {
  ///         	Output verbosity level
  verbose     	: usize,
  ///         	Path of the .keylayout file to parse
  file_in     	: Vec<PathBuf>,
  file_out    	: Vec<PathBuf>,
  ///         	Overwrite output file even if it exists
  is_overwrite	: bool,
}

use bpaf	::{*, long as l, short as s, positional as pos}; // short names to allow starting builders
fn opts() -> OptionParser<OutCliArg> {
  use std::cmp::{min,max};
  let mut d=Doc::default();d.text("Increase the verbosity (max·3) as ");d.literal("-vvv");d.text(" or ");d.literal("-v -v -v");let verbose_h = d;
  let mut d=Doc::default();d.emphasis("← ");d.text("Input  file path(s), 1st");d.emphasis("≝");d.text(FILE_IN [0]);d.text(", 2nd");d.emphasis("≝");d.text(FILE_IN [1]);let file_in_h = d;
  let mut d=Doc::default();d.emphasis("→ ");d.text("Output file path(s), 1st");d.emphasis("≝");d.text(FILE_OUT[0]);d.text(", 2nd");d.emphasis("≝");d.text(FILE_OUT[1]);let file_out_h = d;
  let verbose     	= s('v'	).l("verbose"  	).h(verbose_h             	).req_flag(())
    .many()       	       	               	                          	.map(|xs| min(xs.len(),3));
  let file_in     	= s('i'	).l("input"    	).h(file_in_h             	).argument::<PathBuf>("PATH")
    .many()       	       	               	                          	  .complete_shell(ShellComp::File{mask:Some("*.keylayout"),});
  let file_out    	= s('o'	).l("output"   	).h(file_out_h            	).argument::<PathBuf>("PATH") // but it's optional when rustc can derive it
    .many()       	       	               	                          	  .complete_shell(ShellComp::File{mask:None});
  let is_overwrite	= s('r'	).l("overwrite"	).h("Overwrite ouput file"	).switch();
  let parser      	= construct!(OutCliArg{verbose,file_in,file_out,is_overwrite}); // parser containing info about args
  let parser_opt  	= parser.to_options().version(env!("CARGO_PKG_VERSION")).max_width(160).descr("Process a keyboard layout, save output"); // option parser with metainformation attached
  parser_opt
}

use std::collections::{HashMap,HashSet,BTreeMap};
use std::env;
use std::fs::File;
use std::io::{BufRead,BufReader,Read,BufWriter};

use quick_xml::de::from_str;
use serde::Deserialize;
pub mod xml_schema;
use xml_schema::*;

fn main() -> anyhow::Result<()> { // Result<(), quick_xml::DeError>
  let parser_opt:OptionParser<OutCliArg> = opts();
  let opts = parser_opt.run(); // let _ = pt(&opts);
  let mut klt: Vec<PathBuf> = vec![];
  let mut doc: Vec<PathBuf> = vec![];
  let len_i = opts.file_in .len();
  let len_o = opts.file_out.len();
  if        len_i == 0 {klt.push(FILE_IN [0].into()); klt.push(FILE_IN [1].into());
  } else if len_i == 1 {klt = opts.file_in.clone() ;  klt.push(FILE_IN [1].into());
  } else               {klt = opts.file_in.clone() ;};
  if        len_o == 0 {doc.push(FILE_OUT[0].into()); doc.push(FILE_OUT[1].into());
  } else if len_o == 1 {doc = opts.file_out.clone();  doc.push(FILE_OUT[1].into());
  } else               {doc = opts.file_out.clone();};
  if   len_i >  2
    || len_o >  2 {
    if len_i != len_o { q!("Input {} ≠ {} Output. The # of in/out files must match if > 2 !",len_i,len_o);}
  };
  for (i,x) in klt.iter().enumerate() {let _ = save_all(&x, &doc[i], &opts)?;}
  for (i,x) in klt.iter().enumerate() {let _ = save_raw(&x, &doc[i], &opts)?;}
  Ok(())
}

use anyhow::bail as q;
use std::io::prelude::*;
use icu_properties::{maps, Script, sets, GeneralCategory as GCat};
use unicode_names2::name as uname;
use charname::get_name as unameu;
use heck::*;

use phf::phf_map;
static Key2id:phf::Map<&'static str, u8> = phf_map! {
  "A"              	=>0,"S"=>1,"D"=>2,"F"=>3,"H"=>4,"G"=>5,"Z"=>6,"X"=>7,"C"=>8,"V"=>9,
  "Section mark"   	=>10,
  "B"              	=>11,"Q"=>12,"W"=>13,"E"=>14,"R"=>15,"Y"=>16,"T"=>17,
  "1"              	=>18,"2"=>19,"3"=>20,"4"=>21,"6"=>22,"5"=>23,"9"=>25,"7"=>26,"8"=>28,"0"=>29,
  "="              	=>24,"-"=>27,
  "O"              	=>31,"U"=>32,"I"=>34,"P"=>35,"L"=>37,"J"=>38,"K"=>40,"N"=>45,"M"=>46,
  "]"              	=>30,"["=>33,
  "'"              	=>39,";"=>41,","=>43,"/"=>44,"."=>47,"`"=>50,
  "Return"         	=>36,"Backslash"=>42,"Tab"=>48,"Space"=>49,"Delete"=>51,"Escape"=>53,
  "Command"        	=>55,"Shift"=>56,"Caps lock"=>57,"Option"=>58,"Control"=>59,"Right shift"=>60,"Right option"=>61,"Right control"=>62,
  "Fn"             	=>63,
  "F17"            	=>64,"F18"=>79,"F19"=>80,"F5"=>96,"F6"=>97,"F7"=>98,"F3"=>99,"F8"=>100,"F9"=>101,"F11"=>103,"F13"=>105,"F16"=>106,"F14"=>107,"F10"=>109,"F12"=>111,"F15"=>113,"F4"=>118,"F2"=>120,"F1"=>122,
  "Keypad ."       	=>65,"Keypad *"=>67,"Keypad +"=>69,"Keypad /"=>75,"Keypad -"=>78,"Keypad ="=>81,
  "Keypad 0"       	=>82,"Keypad 1"=>83,"Keypad 2"=>84,"Keypad 3"=>85,"Keypad 4"=>86,"Keypad 5"=>87,"Keypad 6"=>88,"Keypad 7"=>89,"Keypad 8"=>91,"Keypad 9"=>92,
  "Clear"          	=>71,
  "Enter"          	=>76,
  "Yen"            	=>93,/*JIS)*/"Japanese conversion key left"	=>102,"Japanese conversion key right"=>104,
  "Contextual Menu"	=>110, // (Windows keyboards)
  "Help"           	=>114,
  "Home"           	=>115,"Page up"=>116,"Forward delete"=>117,"End"=>119,"Page down"=>121,
  "Left arrow"     	=>123,"Right arrow"=>124,"Down arrow"=>125,"Up arrow"=>126,
  "n/a52"          	=>52,"n/a54"=>54,"n/a66"=>66,"n/a68"=>68,"n/a70"=>70,"n/a77"=>77,"n/a90"=>90,"n/a72"=>72,"n/a73"=>73,"n/a74"=>74,"n/a94"=>94,"n/a95"=>95,"n/a108"=>108,"n/a112"=>112,"n/a127"=>127,
};

static Id2key:phf::Map<u8, &'static str> = phf_map! {
  0u8  	=>"A",1u8=>"S",2u8=>"D",3u8=>"F",4u8=>"H",5u8=>"G",6u8=>"Z",7u8=>"X",8u8=>"C",9u8=>"V",
  10u8 	=>"Section mark",
  11u8 	=>"B",12u8=>"Q",13u8=>"W",14u8=>"E",15u8=>"R",16u8=>"Y",17u8=>"T",
  18u8 	=>"1",19u8=>"2",20u8=>"3",21u8=>"4",22u8=>"6",23u8=>"5",25u8=>"9",26u8=>"7",28u8=>"8",29u8=>"0",
  24u8 	=>"=",27u8=>"-",
  31u8 	=>"O",32u8=>"U",34u8=>"I",35u8=>"P",37u8=>"L",38u8=>"J",40u8=>"K",45u8=>"N",46u8=>"M",
  30u8 	=>"]",33u8=>"[",
  39u8 	=>"'",41u8=>";",43u8=>",",44u8=>"/",47u8=>".",50u8=>"`",
  36u8 	=>"Return",42u8=>"Backslash",48u8=>"Tab",49u8=>"Space",51u8=>"Delete",53u8=>"Escape",
  55u8 	=>"Command",56u8=>"Shift",57u8=>"Caps lock",58u8=>"Option",59u8=>"Control",60u8=>"Right shift",61u8=>"Right option",62u8=>"Right control",
  63u8 	=>"Fn",
  64u8 	=>"F17",79u8=>"F18",80u8=>"F19",96u8=>"F5",97u8=>"F6",98u8=>"F7",99u8=>"F3",100u8=>"F8",101u8=>"F9",103u8=>"F11",105u8=>"F13",106u8=>"F16",107u8=>"F14",109u8=>"F10",111u8=>"F12",113u8=>"F15",118u8=>"F4",120u8=>"F2",122u8=>"F1",
  65u8 	=>"Keypad .",67u8=>"Keypad *",69u8=>"Keypad +",75u8=>"Keypad /",78u8=>"Keypad -",81u8=>"Keypad =",
  82u8 	=>"Keypad 0",83u8=>"Keypad 1",84u8=>"Keypad 2",85u8=>"Keypad 3",86u8=>"Keypad 4",87u8=>"Keypad 5",88u8=>"Keypad 6",89u8=>"Keypad 7",91u8=>"Keypad 8",92u8=>"Keypad 9",
  71u8 	=>"Clear",
  76u8 	=>"Enter",
  93u8 	=>"Yen",/*JIS)*/102u8	=>"Japanese conversion key left",104u8=>"Japanese conversion key right",
  110u8	=>"Contextual Menu", // (Windows keyboards)
  114u8	=>"Help",
  115u8	=>"Home",116u8=>"Page up",117u8=>"Forward delete",119u8=>"End",121u8=>"Page down",
  123u8	=>"Left arrow",124u8=>"Right arrow",125u8=>"Down arrow",126u8=>"Up arrow",
  52u8 	=>"n/a52",54u8=>"n/a54",66u8=>"n/a66",68u8=>"n/a68",70u8=>"n/a70",77u8=>"n/a77",90u8=>"n/a90",72u8=>"n/a72",73u8=>"n/a73",74u8=>"n/a74",94u8=>"n/a94",95u8=>"n/a95",108u8=>"n/a108",112u8=>"n/a112",127u8=>"n/a127",
};
use kdl::KdlDocument;
fn save_raw<K,D>(klt_as:K, doc_as:D, opts:&OutCliArg) -> anyhow::Result<()>
  where K:AsRef<Path> + std::fmt::Debug, D:AsRef<Path> + std::fmt::Debug {
  /*! Converts a .keylayout into a list of keys by layer in that layout in KDL format:
    label sym="" name="labels" { //no-break→ ←space is used as a separator to allow regular spaces to be used as empty keys
      row_1 val=r#"§ 1 2  3 4 5 6 7 8 9  0 - ="#
    r sym="" name="nomod" {
      row_1 val=r#"⎋ ‽   №   ¤  ‸ ‽ ⁂   ⁀ ⹀  "#*/

  let doc:&Path = doc_as.as_ref();
  let klt:&Path = klt_as.as_ref();
  let dbg = opts.verbose;

  let layout_file = File::open(klt)?;
  let layout_s = io::read_to_string(layout_file)?;
  let kbd_layout: Keyboard = from_str(&layout_s)?;

  let mut dead_keys:HashMap<String,DeadKey> = HashMap::new(); //"math∱":DeadKey{name:"math∱",lbl:"🕱∱",output:"∱"},
  for term in kbd_layout.terminators.when {
    if let When::Output{state,output} = term {
      let dk = DeadKey{name:state.clone(),lbl:"🕱".to_string()+&output,output:output};
      dead_keys.insert(state.to_string(),dk);
    }
  }

  Ok(())
}
fn save_all<K,D>(klt_as:K, doc_as:D, opts:&OutCliArg) -> anyhow::Result<()>
  where K:AsRef<Path> + std::fmt::Debug, D:AsRef<Path> + std::fmt::Debug {
  /*! Converts a .keylayout into a SymbolsAll-En_Names.md with a table of all unique symbols in that layout:
    | ␁ | `u+0001` | `&#1;` | Start Of Heading |
   */

  let doc:&Path = doc_as.as_ref();
  let klt:&Path = klt_as.as_ref();
  let dbg = opts.verbose;

  let layout_file = File::open(klt)?;
  let layout_s = io::read_to_string(layout_file)?;
  let kbd_layout: Keyboard = from_str(&layout_s)?;

  let mut set_all = HashSet::new();
  for     kms in kbd_layout.key_map_set {
    for   km  in kms.key_map {
      for key in km.key {
        match key {
          Key::Output{code, ref output} => {/*p!("code={:#?} out={:#?}", code, output)?;*/set_all.insert(output.to_string());},
          Key::Action{code, ref action} => {/*p!("code={:#?} act={:#?}", code, action)?;*/},
        }
      };
    };
  };
  for     act  in kbd_layout.actions.action {
    for   when in act.when {
      match when {
        When::Next  {state, ref next  } => {/*p!("state={:#?} out={:#?}", state, next  )?;*/},
        When::Output{state, ref output} => {/*p!("state={:#?} act={:#?}", state, output)?;*/set_all.insert(output.to_string());},
      }
    };
  };if dbg >= 3 {p!("Created a set of {} unique outputs", set_all.len())?;}

  let mut char_single = BTreeMap::new();
  let mut char_multi  = BTreeMap::new();
  for s in &set_all {
    let count = s.chars().count();
    let mut chars = s.chars();
    if count == 1	{
      match chars.next() {
        None    	=> {},
        Some(ch)	=> {char_single.entry(ch as u32).or_insert(ch);},};
    } else      	   {char_multi .entry(s.clone()).or_insert(s);};
  };if dbg >= 3 {p!("Split {} outputs into {} chars and {} strings", set_all.len(), char_single.len(), char_multi.len())?;}

  if doc.exists() && ! opts.is_overwrite { q!("File exists {:?}, allow overwriting via the -r flag",doc);
  } else {
    let     summary_file	= File::create(doc)?; // Opens a file in write-only mode
    let mut summary_buf 	= BufWriter::new(summary_file);
    writeln!(summary_buf,"| Symbol  | Hex<br>U+… | Dec<br>HTML `&#…;` | Unicode name |")?;
    writeln!(summary_buf,"| :-----: | :--------: | :----------------: | :----------- |")?;
    // writeln!(summary_buf,"|         | U+…  | HTML `&#…;` |              |");

    if dbg >= 3 {p!("Writing {} chars to {:?}", char_single.len(), doc)?;}
    for (id,ch) in char_single {
      let name	= uname( ch).map(|n| n.to_string()).unwrap_or_else(|| unameu(id).to_string());
      let ch_rev = match maps::general_category().get(ch) {
        GCat::Control	=> { // try to get a symbol for a control char instead of printing itself
          let name_sub = match id { // use alternative aliases to match symbols
            0x09	=> "HORIZONTAL TABULATION",
            0x0a	=> "LINE FEED",
            0x0b	=> "VERTICAL TABULATION",
            0x0c	=> "Form Feed",
            0x0d	=> "Carriage Return",
            0x1c	=> "FILE SEPARATOR",
            0x1d	=> "GROUP SEPARATOR",
            0x1e	=> "RECORD SEPARATOR",
            0x1f	=> "UNIT SEPARATOR",
            _   	=> &name,
          };
          unicode_names2::character(&format!("SYMBOL FOR {}",name_sub)).unwrap_or_else(|| ' ')
        }	,
        _	=> ch,
      };
      writeln!(summary_buf,"| {} | `{:04x}` | `{}` | {} |",ch_rev,id,id,AsTitleCase(name))?;}
    if dbg >= 3 {p!("Writing {} strings to {:?}", char_multi.len(), doc)?;}
    for (id,ch) in char_multi  {writeln!(summary_buf,"| {} |            |         | |",ch)?;}
    summary_buf.flush()?;
    p!("Parsed layout {:#?} → ={:#?}", klt, doc)?;
  }
  Ok(())
}
