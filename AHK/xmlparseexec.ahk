;               | Root Element XML files can have only 1 root element, this creates that.
;			 |		       | Optional Path/Filename if you want to use an xml file outside of the scripts directory
;			 |		       |
MyXML:=new XML("RootElement","lib\MyXML.xml") ;Creates or Loads the XML if the file exists
;| Stored object into the name Node
;|		          | Path of the new Element you wish to create
;|		          | 				| Associative Array of Attributes that you want to be in the new element
;|		          | 				|							| A text string that is appended to <node>HERE!</node> but be careful
;|		          | 				|							| If you want to have nodes below this current node do not give it a text value
;|		          | 				|							| 	   | Duplicate, This allows for the same named Element to be at the same level 1=Allow Duplicate
;|		          | 				|							| 	   |
Node:=MyXML.Add("My/New/Path",{Attribute:"Value",Another:"Attribute"},"Text Value",0) ;Create a new Node Element
loop, 5
	Node:=MyXML.Add("My/New/Path",{Attribute:"Value",index:A_Index,Another:"Attribute"},"hello" A_Index+10,1) ;Create a new Node Element

Top:=MyXML.Add("Just_A_Node") ;Create a node on its own


;            | The node object that you created previously
;            | 	| The name for the new node
;            | 	|			| Like above an Associative Array for the Attributes
;            | 	|			|			| Text Value for the Node
;            | 	|			|			|
MyXML.Under(Top,"Node_Name",{Attribute:"Value"},"Text Value")

MyXML.Transform() ;Makes the XML Pretty
MyXML.Transform() ;Sometimes needed.

;~list:=MyXML.SN("//Path") ;Select NODES: build list which has all nodes with the nodename of Path  ;// means look everywhere
;~node:=myxml.SSN("//My/New")
;~list:=SN(node,"Path")
;~while(item:=list.item[a_index-1],obj:=xml.EA(item))
;~m(item.xml,obj.Attribute,obj.index)
;~m(MyXML.SSN("//My/New").xml)
;~m(SSN(Top,"Node_Name").xml) ;first item is ahk object.  then pass what we want from that object
;~m(SSN(Top,"Node_Name").xml) ;first item is ahk object.  then pass what we want from that object

;			     @=Attribute
;~m(MyXML.SSN("//Path[@index='4']").xml) ;//Path gets first.  If want multiple ones (and want specific one) use brackets and @index
;~m(MyXML.SSN("//Path[text()='15']").xml) ;//Path gets first.  If want multiple ones (and want specific one) use brackets and @index
;                   text() =looking for exact text values
;~m(MyXml.SSN("//Path[contains(text(),'lo11')]").xml)
;                   does matching across all path nodes thtat contain text value
                    ;~swap contains(text(),'lol1')  to contains(@Attribute,'" variable "') ;use inside double outside single quotes to pass variable



m(MyXML[]) ;Shows a MsgBox with the contents of the new node
;          1 is to "Make the XML pretty"
MyXML.Save(1) ;Saves the xml
ExitApp

Class XML{
	keep:=[]
	__New(param*){
		if(!FileExist(A_ScriptDir "\lib"))
			FileCreateDir,%A_ScriptDir%\lib
		root:=param.1,file:=param.2,file:=file?file:root ".xml",temp:=ComObjCreate("MSXML2.DOMDocument"),temp.setProperty("SelectionLanguage","XPath"),this.xml:=temp,this.file:=file,xml.keep[root]:=this
		;temp.preserveWhiteSpace:=1
		if(FileExist(file)){
			FileRead,info,%file%
			if(info=""){
				this.xml:=this.CreateElement(temp,root)
				FileDelete,%file%
			}else
				temp.LoadXML(info),this.xml:=temp
		}else
			this.xml:=this.CreateElement(temp,root)
	}CreateElement(doc,root){
		return doc.AppendChild(this.xml.CreateElement(root)).ParentNode
	}Add(path,att:="",text:="",dup:=0){
		p:="/",add:=(next:=this.SSN("//" path))?1:0,last:=SubStr(path,InStr(path,"/",0,0)+1)
		if(!next.xml){
			next:=this.SSN("//*")
			for a,b in StrSplit(path,"/")
				p.="/" b,next:=(x:=this.SSN(p))?x:next.AppendChild(this.xml.CreateElement(b))
		}if(dup&&add)
			next:=next.ParentNode.AppendChild(this.xml.CreateElement(last))
		for a,b in att
			next.SetAttribute(a,b)
		next.text:=text
		return next
	}
	Find(info*){
		static last:=[]
		doc:=info.1.NodeName?info.1:this.xml
		if(info.1.NodeName)
			node:=info.2,find:=info.3,return:=info.4!=""?"SelectNodes":"SelectSingleNode",search:=info.4
		else
			node:=info.1,find:=info.2,return:=info.3!=""?"SelectNodes":"SelectSingleNode",search:=info.3
		if(InStr(info.2,"descendant"))
			last.1:=info.1,last.2:=info.2,last.3:=info.3,last.4:=info.4
		if(InStr(find,"'"))
			return doc[return](node "[.=concat('" RegExReplace(find,"'","'," Chr(34) "'" Chr(34) ",'") "')]/.." (search?"/" search:""))
		else
			return doc[return](node "[.='" find "']/.." (search?"/" search:""))
	}
	Under(under,node,att:="",text:="",list:=""){
		new:=under.AppendChild(this.xml.CreateElement(node)),new.text:=text
		for a,b in att
			new.SetAttribute(a,b)
		for a,b in StrSplit(list,",")
			new.SetAttribute(b,att[b])
		return new
	}ReCreate(path,new){
		rem:=this.SSN(path),rem.ParentNode.RemoveChild(rem),new:=this.Add(new)
		return new
	}SSN(path){
		return this.xml.SelectSingleNode(path)
	}SN(path){
		return this.xml.SelectNodes(path)
	}__Get(x=""){
		return this.xml.xml
	}Get(Path,Default){
		text:=this.SSN(path).text
		return text?text:Default
	}Transform(){
		static
		if(!IsObject(xsl))
			xsl:=ComObjCreate("MSXML2.DOMDocument"),xsl.loadXML("<xsl:stylesheet version=""1.0"" xmlns:xsl=""http://www.w3.org/1999/XSL/Transform""><xsl:output method=""xml"" indent=""yes"" encoding=""UTF-8""/><xsl:template match=""@*|node()""><xsl:copy>`n<xsl:apply-templates select=""@*|node()""/><xsl:for-each select=""@*""><xsl:text></xsl:text></xsl:for-each></xsl:copy>`n</xsl:template>`n</xsl:stylesheet>"),style:=null
		this.xml.transformNodeToObject(xsl,this.xml)
	}Save(x*){
		if(x.1=1)
			this.Transform()
		if(this.xml.SelectSingleNode("*").xml="")
			return m("Errors happened while trying to save " this.file ". Reverting to old version of the XML")
		filename:=this.file?this.file:x.1.1,ff:=FileOpen(filename,0),text:=ff.Read(ff.length),ff.Close()
		if(!this[])
			return m("Error saving the " this.file " xml.  Please get in touch with maestrith if this happens often")
		if(text!=this[])
			file:=FileOpen(filename,"rw"),file.seek(0),file.write(this[]),file.length(file.position)
	}EA(path,att:=""){
		list:=[]
		if(att)
			return path.NodeName?SSN(path,"@" att).text:this.SSN(path "/@" att).text
		nodes:=path.NodeName?path.SelectNodes("@*"):nodes:=this.SN(path "/@*")
		while,n:=nodes.item(A_Index-1)
			list[n.NodeName]:=n.text
		return list
}}
SSN(node,path){
	return node.SelectSingleNode(path)
}
SN(node,path){
	return node.SelectNodes(path)
}
m(x*){
	active:=WinActive("A")
	ControlGetFocus,Focus,A
	ControlGet,hwnd,hwnd,,%Focus%,ahk_id%active%
	static list:={btn:{oc:1,ari:2,ync:3,yn:4,rc:5,ctc:6},ico:{"x":16,"?":32,"!":48,"i":64}},msg:=[],msgbox
	list.title:="AHK Studio",list.def:=0,list.time:=0,value:=0,msgbox:=1,txt:=""
	for a,b in x
		obj:=StrSplit(b,":"),(vv:=List[obj.1,obj.2])?(value+=vv):(list[obj.1]!="")?(List[obj.1]:=obj.2):txt.=b "`n"
	msg:={option:value+262144+(list.def?(list.def-1)*256:0),title:list.title,time:list.time,txt:txt}
	Sleep,120
	MsgBox,% msg.option,% msg.title,% msg.txt,% msg.time
	msgbox:=0
	for a,b in {OK:value?"OK":"",Yes:"YES",No:"NO",Cancel:"CANCEL",Retry:"RETRY"}
		IfMsgBox,%a%
		{
			WinActivate,ahk_id%active%
			ControlFocus,%Focus%,ahk_id%active%
			return b
		}
}
t(x*){
	for a,b in x{
		if((obj:=StrSplit(b,":")).1="time"){
			SetTimer,killtip,% "-" obj.2*1000
			Continue
		}
		list.=b "`n"
	}
	Tooltip,% list
	return
	killtip:
	ToolTip
	return
}