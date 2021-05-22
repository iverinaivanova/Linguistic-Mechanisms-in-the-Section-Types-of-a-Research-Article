/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sectionsretrieval;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Scanner;
import static java.util.stream.DoubleStream.builder;
import static java.util.stream.IntStream.builder;
import org.w3c.dom.Document;

/**
 *
 * @author Administrator
 */
public class IntroRetrieval {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws IOException {
        // TODO code application logic here

        File dir = new File("../papersectionsretrieval/all_xmls");
        File[] files = dir.listFiles();
        String path = "../papersectionsretrieval/acl_anthology_sections/introductions_texts.txt";
        for (File file : files) {
            Scanner scan = new Scanner(file, "UTF-8");
            String contents = "";
            while (scan.hasNextLine()) {
                String myLine = scan.nextLine();
                if (myLine.equals("1 Introduction") || myLine.endsWith("Introduction") || myLine.endsWith("INTRODUCTION") || myLine.endsWith("Problem") || myLine.endsWith("Overwiew") || myLine.endsWith("Motivation") /*|| myLine.contains("Introduction")*/) {
                    while (!(myLine.startsWith("<sectionHeader"))&& scan.hasNextLine()) {
                        myLine = scan.nextLine();
                        // The program skips lines under the following conditions.
                        if (myLine.startsWith("<bodyText confidence") || myLine.startsWith("</bodyText")) {
                            continue;
                        } else if (myLine.startsWith("<table confidence") || myLine.startsWith("</table")) {
                            continue;
                        } else if (myLine.startsWith("<page confidence") || myLine.startsWith("</page")) {
                            continue;
                        } else if (myLine.startsWith("<note confidence") || myLine.startsWith("</note")) {
                            continue;
                        } else if (myLine.startsWith("<footnote confidence") || myLine.startsWith("</footnote")) {
                            continue;
                        } else if (myLine.startsWith("<figureCaption confidence") || myLine.startsWith("</figureCaption")) {
                            continue;
                        } else if (myLine.contains("<figureCaption confidence") || myLine.contains("</figureCaption>")) {
                            continue;
                        } else if (myLine.startsWith("<listItem confidence") || myLine.startsWith("</listItem>")) {
                            continue;
                        } else if (myLine.contains("<listItem confidence") || myLine.contains("</listItem>")) {
                            continue;
                        } else if (myLine.startsWith("<figure confidence") || myLine.startsWith("</figure>")) {
                            continue;
                        } else if (myLine.contains("<figure confidence") || myLine.contains("</figure>")) {
                            continue;
                        } else if (myLine.startsWith("<tableCaption confidence") || myLine.startsWith("</tableCaption>")) {
                            continue;
                        } else if (myLine.startsWith("<equation confidence") || myLine.startsWith("</equation>")) {
                            continue;
                        } else if (myLine.startsWith("<subsectionHeader confidence") || myLine.startsWith("</subsectionHeader>")) {
                            continue;
                        } else if (myLine.contains("<subsectionHeader confidence") || myLine.contains("</subsectionHeader>")) {
                            continue;
                        } else if (myLine.contains("<sectionHeader confidence") || myLine.contains("</sectionHeader>")) {
                            continue; 
                        } else if (myLine.contains("<author confidence") || myLine.contains("</author>")) {
                            continue; 
                        } else if (myLine.startsWith("<section confidence") || myLine.startsWith("</section>")) {
                            continue;
                         } else if (myLine.contains("<construct confidence") || myLine.startsWith("</construct>")) {
                            continue;
                        } else if (myLine.startsWith("</sectionHeader")) {
                            continue;
                        }

                        contents = contents.concat(myLine + "\n");

                    }

                    StringBuilder sb = new StringBuilder();
                    String[] lines = contents.split("\n");
                    for (String l : lines) {
                        //System.out.println("aLine: " + l);
                        if (l.endsWith("-")) {
                            sb.append(l.substring(0, l.length() - 1));

                        } else {
                            sb.append(l + " ");
                        }
                        contents = sb.toString();
                    }
                }
            }
            
           // System.out.println(fileID + "\t" + contents + "\n");
            
            String fileID = file.getName();  
            FileWriter fw = new FileWriter(path, true);
            BufferedWriter bw = new BufferedWriter(fw);
            PrintWriter pw = new PrintWriter(bw);
            //pw.println(fileID + "\t" + contents + "\n");
            pw.println(contents + "\n");
            pw.flush();
            pw.close();

        }

    }
}
