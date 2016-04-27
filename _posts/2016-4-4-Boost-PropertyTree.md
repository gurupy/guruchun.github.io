---
layout: post
title: boost/property-tree 로 XML 파일 읽기/쓰기
---

boost/property-tree를 사용해서 xml 파일을 읽고 쓰는 예제이다. 
계층적 구조를 가지는 xml node와 node의 속성을 읽고, node의 children node들을 읽어 vector에 담는다.

## 읽어들일 XML 파일의 구조

```
<debug>
  <filename>debug.log</filename>
  <modules name1="value1" name2="value2">
    <module attr1="att1-value" attr2="attr2-value-f">Finance</module>
    <module attr1="att1-value" attr2="attr2-value-a">Admin</module>
    <module attr1="att1-value" attr2="attr2-value-h">HR</module>
  </modules>
  <level>2</level>
</debug>
```

## 예제 소스

```
#include <boost\asio.hpp>
#include <boost/property_tree/ptree.hpp>
#include <boost/property_tree/xml_parser.hpp>

#include <iostream>
#include <string>
#include <set>
#include <exception>

using namespace std;
namespace pt = boost::property_tree;

void main()
{
	cout << "start main" << endl;

	string inputPath = "E:/WorksWin/Boost/ConfigMgr/input.xml";

	// Create empty property tree object
	pt::ptree tree;

	// Parse the XML into the property tree.
	pt::read_xml(inputPath, tree);

	// Use the throwing version of get to find the debug filename.
	// If the path cannot be resolved, an exception is thrown.
	string m_file = tree.get<std::string>("debug.filename");
	cout << "debug.filename" << m_file << endl;

	// Use the default-value version of get to find the debug level.
	// Note that the default value is used to deduce the target type.
	int m_level = tree.get("debug.level", 0);
	cout << "debug.level" << m_level << endl;

	// get attr list
	for (const pt::ptree::value_type &v : tree.get_child("debug.modules.<xmlattr>"))
	{
		std::cout << "debug.modules.<xmlattr>:" << v.first <<  std::endl;
	}
	std::cout << std::endl;

	// get child list
	for (const auto &v : tree.get_child("debug.modules.module"))
	{
		std::cout << "debug.modules.module:" << v.first << std::endl;

		string name;
		pt::ptree sub_pt;
		std::tie(name, sub_pt) = v;
		std::cout << name << std::endl;
		std::cout << "\t" << sub_pt.get<std::string>("<xmlattr>.attr1") << std::endl;
		std::cout << "\t" << sub_pt.get<std::string>("<xmlattr>.attr2") << std::endl;
	}
	std::cout << std::endl;

	string key;
	getline(cin, key);
}
```

## 소스 설명
