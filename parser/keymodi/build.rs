#![allow(non_snake_case,non_upper_case_globals,non_camel_case_types,unused_imports,unused_mut,unused_variables,dead_code,unused_assignments,unused_macros)]
// Skips rebuilding if file exists, so need to manually update on data changes
extern crate helper;
extern crate keymodi_data;
use helper        	::*; // gets macros
use helper::alias 	::*;
use helper::helper	::*;
use keymodi_data  	::*;

use std      	::env;
use std::fs  	::File;
use std::io  	::{BufWriter, Write};
use std::path	::Path;

const symLeft_atL 	:[&str;4]	= ["left","left_","left ","‹"];
const symRight_atL	:[&str;3]	= ["right","right_","right "];
const symRight_atR	:[&str;1]	= ["›"];
const symShift    	:[&str;3]	= ["sh","shift","⇧"];
const symCtrl     	:[&str;5]	= ["ctrl","control","⎈","⌃","^"];
const symWinCmd   	:[&str;5]	= ["cmd","command","◆","⌘","❖"];
const symAlt      	:[&str;5]	= ["alt","opt","option","⎇","⌥"];

use indexmap	::{IndexMap, IndexSet};
pub fn prefill_key2bit() -> IndexMap<String,kModiFlag> {
  let mut key2bit:IndexMap<String, kModiFlag> = IndexMap::new();

  for symKey in symShift {
    {const key_bit:kModiFlag = kModiFlag::LShift;
    for symSide  in symLeft_atL  { key2bit.insert(symSide.to_string() + symKey , key_bit );}}
    {const key_bit:kModiFlag = kModiFlag::RShift;
    for symSide  in symRight_atL { key2bit.insert(symSide.to_string() + symKey , key_bit );}
    for symSide  in symRight_atR { key2bit.insert(symKey .to_string() + symSide, key_bit );}}
    {const key_bit:kModiFlag = kModiFlag::Shift;
                                   key2bit.insert(symKey .to_string()          , key_bit ); }  }
  for symKey in symCtrl {
    {const key_bit:kModiFlag = kModiFlag::LCtrl;
    for symSide  in symLeft_atL  { key2bit.insert(symSide.to_string() + symKey , key_bit );}}
    {const key_bit:kModiFlag = kModiFlag::RCtrl;
    for symSide  in symRight_atL { key2bit.insert(symSide.to_string() + symKey , key_bit );}
    for symSide  in symRight_atR { key2bit.insert(symKey .to_string() + symSide, key_bit );}}
    {const key_bit:kModiFlag = kModiFlag::Ctrl;
                                   key2bit.insert(symKey .to_string()          , key_bit ); }  }
  for symKey in symWinCmd {
    {const key_bit:kModiFlag = kModiFlag::LWinCmd;
    for symSide  in symLeft_atL  { key2bit.insert(symSide.to_string() + symKey , key_bit );}}
    {const key_bit:kModiFlag = kModiFlag::RWinCmd;
    for symSide  in symRight_atL { key2bit.insert(symSide.to_string() + symKey , key_bit );}
    for symSide  in symRight_atR { key2bit.insert(symKey .to_string() + symSide, key_bit );}}
    {const key_bit:kModiFlag = kModiFlag::WinCmd;
                                   key2bit.insert(symKey .to_string()          , key_bit ); }  }
  for symKey in symAlt {
    {const key_bit:kModiFlag = kModiFlag::LAlt;
    for symSide  in symLeft_atL  { key2bit.insert(symSide.to_string() + symKey , key_bit );}}
    {const key_bit:kModiFlag = kModiFlag::RAlt;
    for symSide  in symRight_atL { key2bit.insert(symSide.to_string() + symKey , key_bit );}
    for symSide  in symRight_atR { key2bit.insert(symKey .to_string() + symSide, key_bit );}}
    {const key_bit:kModiFlag = kModiFlag::Alt;
                                   key2bit.insert(symKey .to_string()          , key_bit ); }  }
  // for (k,v) in key2bit.iter() { p!("{k}={v}");  }
  // key2bit= right⎇=RAlt right_⎇=RAlt ⎇›=RAlt ... ⌥=LAlt | RAlt ordered from left/right keys to either
  key2bit
}
fn main() {
  let     path	= Path     ::new("./../build").join("key2bit_codegen.rs");
  if      path	.exists(){pb!("skip rebuilding existing file={:?}",&path.as_os_str());return ()};
  let mut file	= BufWriter::new(File::create(&path).unwrap());
  pb!("path={:?}",&path.as_os_str());

  let key2bit = prefill_key2bit();
  let mut phf_key2bit = phf_codegen::OrderedMap::new();
  for (key, value) in key2bit {phf_key2bit.entry(key, &format!("{:?}",value));}
  write!(&mut file, "static key2bit: phf::OrderedMap<&'static str, kModiFlag> = {}", phf_key2bit.build()).unwrap();
  write!(&mut file, ";\n").unwrap();
}
