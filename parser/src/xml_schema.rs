// generated with the help of github.com/Thomblin/xml_schema_generator
use serde::{Deserialize,Serialize};
#[derive(Serialize,Deserialize)] pub struct Keyboard {
  #[serde(rename="@group"     	)] pub group       	: String,
  #[serde(rename="@id"        	)] pub id          	: String,
  #[serde(rename="@name"      	)] pub name        	: String,
  #[serde(rename="@maxout"    	)] pub maxout      	: String,
  #[serde(rename="$text"      	)] pub text        	: Option<String>,
  pub                         	       layouts     	: Layouts,
  #[serde(rename="modifierMap"	)] pub modifier_map	: ModifierMap,
  #[serde(rename="keyMapSet"  	)] pub key_map_set 	: Vec<KeyMapSet>,
  pub                         	       actions     	: Actions,
  pub                         	       terminators 	: Terminators,
}
#[derive(Serialize,Deserialize)] pub struct Layouts {
  #[serde(rename="$text"	)] pub text  	: Option<String>,
  pub                   	       layout	: Vec<Layout>,
}
#[derive(Serialize,Deserialize)] pub struct Layout {
  #[serde(rename="@first"    	)] pub first    	: String,
  #[serde(rename="@last"     	)] pub last     	: String,
  #[serde(rename="@mapSet"   	)] pub map_set  	: String,
  #[serde(rename="@modifiers"	)] pub modifiers	: String,
}
#[derive(Serialize,Deserialize)] pub struct ModifierMap {
  #[serde(rename="@id"          	)] pub id            	: String,
  #[serde(rename="@defaultIndex"	)] pub default_index 	: String,
  #[serde(rename="$text"        	)] pub text          	: Option<String>,
  #[serde(rename="keyMapSelect" 	)] pub key_map_select	: Vec<KeyMapSelect>,
}
#[derive(Serialize,Deserialize)] pub struct KeyMapSelect {
  #[serde(rename="@mapIndex"	)] pub map_index	: String,
  #[serde(rename="$text"    	)] pub text     	: Option<String>,
  pub                       	       modifier 	: Vec<Modifier>,
}
#[derive(Serialize,Deserialize)] pub struct Modifier {
  #[serde(rename="@keys"	)] pub keys	: String,
}
#[derive(Serialize,Deserialize)] pub struct KeyMapSet {
  #[serde(rename="@id"   	)] pub id     	: String,
  #[serde(rename="$text" 	)] pub text   	: Option<String>,
  #[serde(rename="keyMap"	)] pub key_map	: Vec<KeyMap>,
}
#[derive(Serialize,Deserialize)] pub struct KeyMap {
  #[serde(rename="@index"     	)] pub index       	: String,
  #[serde(rename="@baseIndex" 	)] pub base_index  	: Option<String>,
  #[serde(rename="@baseMapSet"	)] pub base_map_set	: Option<String>,
  #[serde(rename="$text"      	)] pub text        	: Option<String>,
  pub                         	       key         	: Vec<Key>,
}
#[derive(Serialize,Deserialize)] pub struct Key {
  #[serde(rename="@code"  	)] pub code  	: String,
  #[serde(rename="@action"	)] pub action	: Option<String>,
  #[serde(rename="@output"	)] pub output	: Option<String>,
}
#[derive(Serialize,Deserialize)] pub struct Actions {
  #[serde(rename="$text"	)] pub text  	: Option<String>,
  pub                   	       action	: Vec<Action>,
}
#[derive(Serialize,Deserialize)] pub struct Action {
  #[serde(rename="@id"  	)] pub id  	: String,
  #[serde(rename="$text"	)] pub text	: Option<String>,
  pub                   	       when	: Vec<ActionWhen>,
}
#[derive(Serialize,Deserialize)] pub struct ActionWhen {
  #[serde(rename="@state" 	)] pub state 	: String,
  #[serde(rename="@next"  	)] pub next  	: Option<String>,
  #[serde(rename="@output"	)] pub output	: Option<String>,
}
#[derive(Serialize,Deserialize)] pub struct Terminators {
  #[serde(rename="$text"	)] pub text	: Option<String>,
  pub                   	       when	: Vec<TerminatorsWhen>,
}
#[derive(Serialize,Deserialize)] pub struct TerminatorsWhen {
  #[serde(rename="@state" 	)] pub state 	: String,
  #[serde(rename="@output"	)] pub output	: String,
}
