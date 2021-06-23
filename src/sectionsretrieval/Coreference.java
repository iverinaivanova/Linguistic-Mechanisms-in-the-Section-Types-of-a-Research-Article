/*
 * The script retrieves the sentence count and the total number of coreference chains per article section using
 * the Stanford CoreNLP Module.
 */
package sectionsretrieval;

import edu.stanford.nlp.coref.data.CorefChain;
import edu.stanford.nlp.ling.CoreLabel;
import edu.stanford.nlp.pipeline.CoreDocument;
import edu.stanford.nlp.pipeline.CoreSentence;
import edu.stanford.nlp.pipeline.StanfordCoreNLP;
import edu.stanford.nlp.trees.Tree;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.Properties;
import java.util.Scanner;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

public class Coreference {

    public static void main(String... args) throws ParserConfigurationException, SAXException, IOException {
       Properties props = new Properties();
        // set the list of annotators to run
        props.setProperty("annotators", "tokenize,ssplit,pos,lemma,ner,parse,depparse,coref,sentiment,kbp,quote");
        // set a property for an annotator, in this case the coref annotator is being set to use the neural algorithm
        props.setProperty("coref.algorithm", "neural");
        // build pipeline
        StanfordCoreNLP pipeline = new StanfordCoreNLP(props);

        // Add the path to the input xml files
        File[] files = new File("../all_xmls").listFiles();
        Arrays.sort(files);
        analyzeFiles(files, pipeline);
    }

    public static void analyzeFiles(File[] files, StanfordCoreNLP pipeline) throws ParserConfigurationException, SAXException, IOException {

        //Extracting the Introduction section, which can spread over several <bodyText> sections
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        DocumentBuilder builder = factory.newDocumentBuilder();
        String path = "../introductions.txt";
        for (File file : files) {
            Document doc = (Document) builder.parse(file);
            //System.out.println("Analysing file: " + file.getName());
            ArrayList<String> list = new ArrayList<>();
            // System.out.println(fileID);
            // System.out.println("------------------------------------------");
            Scanner scan = new Scanner(file, "UTF-8");
            String contents = "";
            while (scan.hasNextLine()) {
                String myLine = scan.nextLine();
                // It is set to extract the sentence count and the coreference chains from the introduction sections.
                if (myLine.equals("1 Introduction") || myLine.endsWith("Introduction")) {
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
            CoreDocument document = new CoreDocument(contents);
            pipeline.annotate(document);
            List<CoreSentence> sentencesOfDoc;
            sentencesOfDoc = document.sentences();
            // Total number of sentences
            int sentCount = document.sentences().size();
            // Getting the corefchains in the document
            Map<Integer, CorefChain> corefChains = document.corefChains();
            int corefNum = corefChains.size();
            //System.out.println(contents);
            String fileID = file.getName();
            System.out.println(fileID);
            System.out.println(document);
            System.out.println(corefChains);
            System.out.println(corefNum);
         }

    }

}


