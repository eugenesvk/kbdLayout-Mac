// generated with the help of github.com/Thomblin/xml_schema_generator
use serde::{Deserialize,Serialize};
#[derive(Debug,Serialize,Deserialize)] pub struct Keyboard { //L0 <keyboard group="126" id="-7151" name="TypES" maxout="3">
  #[serde(rename="@group"     	)] pub group       	: u16,
  #[serde(rename="@id"        	)] pub id          	: i32,
  #[serde(rename="@name"      	)] pub name        	: String,
  #[serde(rename="@maxout"    	)] pub maxout      	: String,
  #[serde(rename="$text"      	)] pub text        	: Option<String>,
  pub                         	       layouts     	: Layouts,
  #[serde(rename="modifierMap"	)] pub modifier_map	: ModifierMap,
  #[serde(rename="keyMapSet"  	)] pub key_map_set 	: Vec<KeyMapSet>,
  pub                         	       actions     	: Actions,
  pub                         	       terminators 	: Terminators,
}
#[derive(Debug,Serialize,Deserialize)] pub struct Layouts { //L1
  #[serde(rename="$text"	)] pub text  	: Option<String>,
  pub                   	       layout	: Vec<Layout>,
}
#[derive(Debug,Serialize,Deserialize)] pub struct Layout { //L2 <layout first="0" last="17" mapSet="16c" modifiers="f4"/>
  #[serde(rename="@first"    	)] pub first    	: u16,
  #[serde(rename="@last"     	)] pub last     	: u16,
  #[serde(rename="@mapSet"   	)] pub map_set  	: String,
  #[serde(rename="@modifiers"	)] pub modifiers	: String,
}
#[derive(Debug,Serialize,Deserialize)] pub struct ModifierMap {
  #[serde(rename="@id"          	)] pub id            	: String,
  #[serde(rename="@defaultIndex"	)] pub default_index 	: u16,
  #[serde(rename="$text"        	)] pub text          	: Option<String>,
  #[serde(rename="keyMapSelect" 	)] pub key_map_select	: Vec<KeyMapSelect>,
}
#[derive(Debug,Serialize,Deserialize)] pub struct KeyMapSelect {
  #[serde(rename="@mapIndex"	)] pub map_index	: u16,
  #[serde(rename="$text"    	)] pub text     	: Option<String>,
  pub                       	       modifier 	: Vec<Modifier>,
}
#[derive(Debug,Serialize,Deserialize)] pub struct Modifier {
  #[serde(rename="@keys"	)] pub keys	: String,
}
#[derive(Debug,Serialize,Deserialize)] pub struct KeyMapSet {
  #[serde(rename="@id"   	)] pub id     	: String,
  #[serde(rename="$text" 	)] pub text   	: Option<String>,
  #[serde(rename="keyMap"	)] pub key_map	: Vec<KeyMap>,
}
#[derive(Debug,Serialize,Deserialize)] pub struct KeyMap {
  #[serde(rename="@index"     	)] pub index       	: u16,
  #[serde(rename="@baseIndex" 	)] pub base_index  	: Option<String>,
  #[serde(rename="@baseMapSet"	)] pub base_map_set	: Option<String>,
  #[serde(rename="$text"      	)] pub text        	: Option<String>,
  pub                         	       key         	: Vec<Key>,
}
#[derive(Debug,Serialize,Deserialize)] pub struct Key {
  #[serde(rename="@code"  	)] pub code  	: String,
  #[serde(rename="@action"	)] pub action	: Option<String>,
  #[serde(rename="@output"	)] pub output	: Option<String>,
}
#[derive(Debug,Serialize,Deserialize)] pub struct Actions {
  #[serde(rename="$text"	)] pub text  	: Option<String>,
  pub                   	       action	: Vec<Action>,
}
#[derive(Debug,Serialize,Deserialize)] pub struct Action {
  #[serde(rename="@id"  	)] pub id  	: String,
  #[serde(rename="$text"	)] pub text	: Option<String>,
  pub                   	       when	: Vec<ActionWhen>,
}
#[derive(Debug,Serialize,Deserialize)] pub struct ActionWhen {
  #[serde(rename="@state" 	)] pub state 	: String,
  #[serde(rename="@next"  	)] pub next  	: Option<String>,
  #[serde(rename="@output"	)] pub output	: Option<String>,
}
#[derive(Debug,Serialize,Deserialize)] pub struct Terminators {
  #[serde(rename="$text"	)] pub text	: Option<String>,
  pub                   	       when	: Vec<TerminatorsWhen>,
}
#[derive(Debug,Serialize,Deserialize)] pub struct TerminatorsWhen {
  #[serde(rename="@state" 	)] pub state 	: String,
  #[serde(rename="@output"	)] pub output	: String,
}
