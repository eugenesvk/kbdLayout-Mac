use std::error::Error;
use std::result;

use crate::alias::*;

type Result<T> = result::Result<T, Box<dyn Error>>;
// pub allows use in other files
pub fn type_of      <T>(_: T) -> &'static str	{         type_name::<T>() }
pub fn print_type_of<T>(_:&T) -> Result<()>  	{p!("{}", type_name::<T>())?; Ok(())}
