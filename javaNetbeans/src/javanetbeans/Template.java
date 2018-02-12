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
import java.nio.file.StandardOpenOption;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/**
 *
 * @author lrospocher
 */
public class Template {

    public static void main(String args[]) throws IOException {

        List<String> list = new ArrayList<>();
        Path pathInput = Paths.get("..//input.in");
        Path pathOutput = Paths.get("..//output.out");

        // Read file and close it automaticaly
        try (Stream<String> stream = Files.lines(Paths.get(pathInput.toUri()))) {
            list = stream
                    .filter(line -> !line.startsWith("line3"))
                    .map(String::toUpperCase)
                    .collect(Collectors.toList());

        } catch (IOException e) {
            e.printStackTrace();
        }

        // DO STUFF
        
        // Print file
        StringBuilder outputStream = new StringBuilder();
        list.forEach( s -> outputStream.append(s + "\n"));
        Files.write(pathOutput, outputStream.toString().getBytes());
    }
}
