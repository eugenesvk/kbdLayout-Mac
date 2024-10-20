use crate::helper::*; // pub use reexports for use in other files
pub use std          	::println      	as pp	; // requires text editor's syntax theme override to retain syntax highlighting
pub use std          	::eprintln     	as pe	;
pub use std          	::writeln      	as w 	;
pub use crate::helper	::print_type_of	as pt	;
pub use std::any     	::type_name    	     	; // for type_of

#[macro_export] macro_rules! pb { // println! during build
  ($($tokens:tt)*) => {println!("cargo:warning={}", format!($($tokens)*))}}
  pub(crate) use pb; // use macro across module boundaries
pub use std::io::{self,Write};
#[macro_export] macro_rules! p  { // println! without panics, propagates error
  ($($tokens:tt)*) => {writeln!(io::stdout(), $($tokens)*)}}
  pub(crate) use p ;
