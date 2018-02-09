/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javanetbeans;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/**
 *
 * @author lrospocher
 */
public class Template {

    public static void main(String args[]) {
        
        List<String> list = new ArrayList<>();
        Path p = Paths.get("..//input.in");
        
        try (Stream<String> stream = Files.lines(Paths.get(p.toUri()))) {
            list = stream
                    .filter(line -> !line.startsWith("line3"))
                    .map(String::toUpperCase)
                    .collect(Collectors.toList());

        } catch (IOException e) {
            e.printStackTrace();
        }

        // DO STUFF
        list.forEach(System.out::println);
    }
}
