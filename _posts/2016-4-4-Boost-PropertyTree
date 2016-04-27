---
layout: post
title: boost/property-tree 로 XML 파일 읽기/쓰기
---

boost/property-tree를 사용해서 xml 파일을 읽고 쓰는 예제이다. 
계층적 구조를 가지는 xml node와 node의 속성을 읽고, node의 children node들을 읽어 vector에 담는다.

## 읽어들일 XML 파일의 구조

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
	string outputPath = "E:/WorksWin/Boost/ConfigMgr/input-out.xml";

	// Create empty property tree object
	pt::ptree tree;

	// Parse the XML into the property tree.
	pt::read_xml(inputPath, tree);

	// Use the throwing version of get to find the debug filename.
	// If the path cannot be resolved, an exception is thrown.
	string m_file = tree.get<std::string>("debug.filename");
	cout << "debug.filename" << m_file;

	// Use the default-value version of get to find the debug level.
	// Note that the default value is used to deduce the target type.
	int m_level = tree.get("debug.level", 0);
	cout << "debug.level" << m_level;

	string key;
	getline(cin, key);
}
```

## 소스 설명
