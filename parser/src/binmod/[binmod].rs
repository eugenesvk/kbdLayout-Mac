extern crate helper;
use ::helper        	::*; // gets macros :: prefix needed due to proc macro expansion
use helper_proc     	::*; // gets proc macros
use ::helper::alias 	::*;
use ::helper::helper	::*;
// use crate::*;

pub fn print42() { p!("{}",42); }
