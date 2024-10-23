#![allow(non_snake_case,non_upper_case_globals,non_camel_case_types,unused_imports,unused_mut,unused_variables,dead_code,unused_assignments,unused_macros)]

use helper::alias 	::*;
use helper::helper	::*;
use keymodi_proc  	::*;

use std::{fmt, str};
use bitflags::bitflags;

#[repr(transparent)] #[derive(Default // use if default value = 0 (same value as calling empty() on the generated struct)
  ,Clone,Copy,PartialEq,Eq,PartialOrd,Ord,Hash // Debug manually to have `Struct::Field1 | Struct::Field2`
  ,AsStrr // print struct name as a string ↑
  )]
pub struct kModiFlag(u32); // define a newtype outside of bitflags macro to support custom derives https://github.com/bitflags/bitflags/blob/main/examples/custom_derive.rs

bitflags! { impl kModiFlag:u32 {
  // const None     	= 0b_____________0; //   0 0-flags: treated as always present; ignored when testing for emptiness
  const LShift      	= 0b_____________1; //   1 ‹⇧
  const LCtrl       	= 0b____________10; //   2 ‹⎈
  const LWinCmd     	= 0b___________100; //   4 ‹◆ = ❖ Windows or ⌘ Mac  aka Super, hijacked Meta's symbol for for either Win or Cmd
  const LAlt        	= 0b__________1000; //   8 ‹⎇
  const RShift      	= 0b_________10000; //  16 ⇧›
  const RCtrl       	= 0b________100000; //  32 ⎈›
  const RWinCmd     	= 0b_______1000000; //  64 ◆› = ❖› Windows or ⌘› Mac
  const RAlt        	= 0b______10000000; // 128 ⎇›
  // const LHyper   	= 0b_____100000000; // 256 ‹✦ ‹✧
  // const LMeta    	= 0b____1000000000; // 512 ‹◆
  // const RHyper   	= 0b___10000000000; //1024 ✦› ✧›
  // const RMeta    	= 0b__100000000000; //2048 ◆›
  // const Caps_lock	= 0b_1000000000000; //4096 ⇪
  // const Num_lock 	= 0b10000000000000; //8192 🔢
  const LWin        	= Self::LWinCmd.bits(); const RWin = Self::RWinCmd.bits();
  const LCmd        	= Self::LWinCmd.bits(); const RCmd = Self::RWinCmd.bits();
  const Win         	= Self::LWin.bits()   	| Self::RWin.bits();
  const Cmd         	= Self::LCmd.bits()   	| Self::RCmd.bits();
  const Shift       	= Self::LShift.bits() 	| Self::RShift.bits();
  const Ctrl        	= Self::LCtrl.bits()  	| Self::RCtrl.bits();
  const WinCmd      	= Self::LWinCmd.bits()	| Self::RWinCmd.bits();
  const Alt         	= Self::LAlt.bits()   	| Self::RAlt.bits();
  const Left        	= Self::LShift.bits() 	| Self::LCtrl.bits() | Self::LWinCmd.bits() | Self::LAlt.bits();
  const Right       	= Self::RShift.bits() 	| Self::RCtrl.bits() | Self::RWinCmd.bits() | Self::RAlt.bits();
  // const Hyper    	= Self::LHyper.bits() 	| Self::RHyper.bits();
  // const Meta     	= Self::LMeta.bits()  	| Self::RMeta.bits();
  }}

/** Write a flag names as text prefixed with struct name `Flags::A | Flags::B` in a bar|separated|format
Ignore unknown flags */
use core::fmt::Write;
use bitflags::{Bits, Flags};
pub fn to_writer_with_struct<B:Flags>(struct_name:&str,flags:&B, mut writer:impl Write) -> Result<(),fmt::Error> {
  let mut first = true;
  let mut iter = flags.iter_names();
  for (name, x) in &mut iter { // Iterate over known flag values
    // if !first {writer.write_str(" | ")?;}; first = false; // | is not const until const_trait_impl is stabilized
    if !first {writer.write_str(".union(")?;};
    writer.write_str(struct_name)?;
    writer.write_str("::")?;
    writer.write_str(name)?;
    if !first {writer.write_str(")")?;};
    first = false;
  }
  fmt::Result::Ok(())
}
impl fmt::Debug   for kModiFlag {fn fmt(&self, f:&mut fmt::Formatter) -> fmt::Result {to_writer_with_struct("kModiFlag",self, f)} }
impl fmt::Display for kModiFlag {fn fmt(&self, f:&mut fmt::Formatter) -> fmt::Result {bitflags::parser::to_writer(      self, f)}}
// impl fmt::Debug   for kModiFlag	{fn fmt(&self, f:&mut fmt::Formatter) -> fmt::Result {fmt::Debug  ::fmt(&self.0,f)}}
// impl fmt::Display for kModiFlag	{fn fmt(&self, f:&mut fmt::Formatter) -> fmt::Result {fmt::Display::fmt(&self.0,f)}}
impl str::FromStr for kModiFlag   	{
  type Err = std::num::ParseIntError; // not a bitflags type anymore, so no bitflags::parser::ParseError
  fn from_str(flags:&str) -> Result<Self, Self::Err> {Ok(Self(flags.parse()?))}
}
// impl str::AsStr   for kModiFlag	{fn as_str(flags:&str) -> fmt::Result {Ok(Self(flags.parse()?))}}

// impl str::AsStr for CategoryType {
//   fn as_str(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
//         bitflags::parser::to_writer(self, f)
    // }
// }
