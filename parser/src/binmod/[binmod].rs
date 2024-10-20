extern crate helper;
use ::helper        	::*; // gets macros :: prefix needed due to proc macro expansion
use helper_proc     	::*; // gets proc macros
use ::helper::alias 	::*;
use ::helper::helper	::*;
// use crate::*;

use std::error::Error;
use std::result;

type Result<T> = result::Result<T, Box<dyn Error>>;
pub fn print42() -> Result<()> {p!("{}",42)?; Ok(())}
