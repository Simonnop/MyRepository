package com.su.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class HelloController {

    @RequestMapping("/h1")
    public String hello(Model model){
        // 封装数据
        model.addAttribute("msg", "Hello,SpringMVC-Annotation");

        return "hello";  // 会被视图解析器处理
    }
}
