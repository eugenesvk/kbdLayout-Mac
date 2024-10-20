#![allow(unused_imports,unused_variables,unreachable_code,dead_code,non_upper_case_globals)]
extern crate helper;
use helper            	::*; // gets macros
pub use helper_proc   	::*; // gets proc macros
pub use helper::alias 	::*;
pub use helper::helper	::*;

_mod!(binmod); //→ #[path="binmod/[binmod].rs"] pub mod binmod;
use crate::binmod::print42;

fn main() {
  print42();
}
