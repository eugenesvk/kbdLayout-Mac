#![allow(non_snake_case,non_upper_case_globals,non_camel_case_types,unused_imports,unused_mut,unused_variables,dead_code,unused_assignments,unused_macros)]

use proc_macro::{TokenStream,TokenTree};
#[proc_macro_derive(AsStr)] pub fn derive_as_string(item:TokenStream) -> TokenStream {
  let mut it = item.into_iter();
  while let Some(tt) = it.next() { match tt {
    TokenTree::Ident(id) => {
      if id.to_string() == "struct" {
        let struct_name = it.next().unwrap().to_string();
        return format!(r#"pub trait AsStr {{fn as_str(&self) -> &'static str;           }}
          impl AsStr for {}               {{fn as_str(&self) -> &'static str {{ "{}" }} }}"#
          ,         struct_name,                                            struct_name).parse().unwrap()
      }}
    _                    => {}
  }}
  panic!("no ident found")
}
