---
layout: post
title: std::map 사용하기, string, vector, user class
---

Simple Map
----------
### Initialize 
`Map<string, string>`
```
std::map<std::string, std::string> const dict {
  "NYC", "LA", "Chicago"
};
```
### get
### set
### insert
### remove

Map with Vector
---------------
### Initialize
`Map<string, vector<string>>`
```
std::map<std::string, std::vector<std::string>> const dict {
   { "USA", { "NYC", "LA", "Chicago" } },
   { "India", { "Delhi", "Bombay" }    }
};
```

Map with User-defined class
---------------------------
### Initialize
```
struct MyClass {   
    unsigned short _addr;
    string _tag;   
    int _dataType; 
    unsigned short _scale;
};
```

### insert
```
map <unsigned short, MyClass> const myData;
mapData[0] = MyClass(0, "tagName.0", 1, 10);
mapData[1] = MyClass(1, "tagName.1", 2, 10);
mapData[2] = MyClass(2, "tagName.2", 2, 10);
mapData[3] = MyClass(3, "tagName.3", 2, 10);
mapData[4] = MyClass(4, "tagName.4", 2, 10);
mapData[5] = MyClass(5, "tagName.5", 2, 10);
```
