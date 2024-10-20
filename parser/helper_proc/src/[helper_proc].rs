#![cfg_attr(not(debug_assertions),allow(non_snake_case,non_upper_case_globals,non_camel_case_types))]
#![cfg_attr(    debug_assertions ,allow(non_snake_case,non_upper_case_globals,non_camel_case_types,unused_imports,unused_mut,unused_variables,dead_code,unused_assignments,unused_macros))]

use proc_macro::{TokenStream,TokenTree};
/// Rewrites path of module imports in a folder to 'modname/[modname].rs', idea from <users.rust-lang.org/t/rename-mod-rs-to-mod-rs/37688/6>
#[proc_macro] pub fn _mod(item:TokenStream) -> TokenStream {
  let ret = format!(r#"#[path="{}/[{}].rs"] pub mod {};"#
    , item,item,item).parse().unwrap();
  ret
}
