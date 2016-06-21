---
layout: post
title: C++ Using Property File (.properties, .ini)
---

Read/write property file (java .properties or windows .ini style)
----------

### Example
```
Propertis properties;
properties.load("xxx.ini");
cout << properties.get("aaa");
propertis.set("aaa", "new value");
```

### Properties.h
```
#include <map>
#include <string>

class Properties {
public:
	bool iskey(const std::string& key);
	std::string get(const std::string& key);
	void set(const std::string& key, const std::string& value);

	void load(std::string& propertyFile);
	void save(std::string& propertyFile);

private:
	std::map<std::string, std::string> _properties;
};
```
### Properties.cpp
```
#include "Properties.h"

#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

// TODO update this class with boost::property_tree

bool Properties::iskey(const string& key) {
	return _properties.count(key) != 0;
}

string Properties::get(const string& key) {
	return _properties.at(key);
}

void Properties::set(const string& key, const string& value) {
	_properties[key] = value;
}

//---------------------------------------------------------------------------
// Reads property file until EOF.
// Invalid data is ignored.
void Properties::load(string& propertyFile) {
	string s, key, value;

	// open file
	ifstream ins;
	ins.open(propertyFile, ifstream::in);

	// For each (key, value) pair in the file
	while (std::getline(ins, s)) {
		size_t begin = s.find_first_not_of(" \f\t\v");

		// Skip blank lines
		if (begin == string::npos) {
			continue;
		}

		// Skip commentary
		if (string("#;").find(s[begin]) != string::npos) {
			continue;
		}

		// Extract the key value
		size_t end = s.find('=', begin);
		if (end == string::npos)
			continue;
		key = s.substr(begin, end - begin);

		// (No leading or trailing whitespace allowed)
		key.erase(key.find_last_not_of(" \f\t\v") + 1);

		// No blank keys allowed
		if (key.empty())
			continue;

		// Extract the value (no leading or trailing whitespace allowed)
		begin = s.find_first_not_of(" \f\n\r\t\v", end + 1);
		end = s.find_last_not_of(" \f\n\r\t\v") + 1;

		value = s.substr(begin, end - begin);

		// Insert the properly extracted (key, value) pair into the map
		_properties[key] = value;
	}
	ins.close();

	// for debugging
//	stringstream ss;
//    for (auto kv : _properties) {
//        ss << kv.first << "=" << kv.second << endl;
//    }
//	cout << "properties:" + ss.str();
}
//---------------------------------------------------------------------------

void Properties::save(string& propertyFile) {
	ofstream outs;
	outs.open(propertyFile, ifstream::out);

    for (auto kv : _properties) {
        outs << kv.first << " = " << kv.second << endl;
    }
    outs.close();
}
```
