#![allow(unused_imports,unused_variables,unreachable_code,dead_code,non_upper_case_globals)]
extern crate helper;
use helper            	::*; // gets macros
pub use helper_proc   	::*; // gets proc macros
pub use helper::alias 	::*;
pub use helper::helper	::*;

_mod!(binmod); //→ #[path="binmod/[binmod].rs"] pub mod binmod;
use crate::binmod::print42;

use std::error::Error;
use std::result;

type Result<T> = result::Result<T, Box<dyn Error>>;
fn main() -> Result<()> {
  print42()?;
use std::str    	::FromStr;
use bpaf        	::{*, long as l, short as s, positional as pos}; // short names to allow starting builders
use bpaf::params	::{NamedArg, ParseArgument, ParsePositional};
pub trait BpafAlias { // add wrapper trait to allow using shorter .l options to continue builders
  fn s     (self, short:char        ) -> Self                                      	;
  fn l     (self, long :&'static str) -> Self                                      	;
  fn h  <M>(self, help :M           ) -> Self             where M:Into<Doc>        	;
  fn arg<T>(self, arg  :&'static str) -> ParseArgument<T> where T:FromStr + 'static	; }
impl      BpafAlias for NamedArg {
  fn s     (self, short:char        ) -> Self                                       {self.short   (short)}
  fn l     (self, long :&'static str) -> Self                                       {self.long    (long )}
  fn h  <M>(self, help :M           ) -> Self             where M:Into<Doc>         {self.help    (help )}
  fn arg<T>(self, arg  :&'static str) -> ParseArgument<T> where T:FromStr + 'static {self.argument(arg  )} }
pub trait BpafAliasPos { // ... for positional arguments
  fn h  <M>(self, help :M           ) -> Self             where M:Into<Doc>	;  }
impl<T>   BpafAliasPos for ParsePositional<T> {
  fn h  <M>(self, help :M           ) -> Self             where M:Into<Doc>         {self.help    (help )}
}
  Ok(())
}

use anyhow::bail as q;
use std::io::prelude::*;
use icu_properties::{maps, Script, sets, GeneralCategory as GCat};
use unicode_names2::name as uname;
use charname::get_name as unameu;
use heck::*;

fn save_all<K,D>(klt_as:K, doc_as:D, opts:&OutCliArg) -> anyhow::Result<()>
  where K:AsRef<Path> + std::fmt::Debug, D:AsRef<Path> + std::fmt::Debug {
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
