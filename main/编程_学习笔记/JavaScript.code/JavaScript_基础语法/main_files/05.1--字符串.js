
/* 
    数据类型: 字面量的类型

    JS中一共有六种数据类型
        String 字符串
        Number 数值
        Boolean 布尔值
        Null 空值
        Undedefined 未定义
        Object 对象

    前五种:基本数据类型
    Object:引用数据类型

    String字符串
        - 在JS中字符串需要使用引号引起来
        - 双引号单引号都可以,但不要混着用
        - 引号不能嵌套.双引号不能放双引号,单引号不能放单引号

*/

var str = "hello";

/* 
    在字符串中,可以使用 \ 作为转义字符,可表示一些特殊符号

        \"  表示 "
        \'  表示 '
        \n  表示换行
        \t  制表符
        \\  表示 \
*/

str = "我说\"今天天气真不错\"";

console.log(str);
