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
