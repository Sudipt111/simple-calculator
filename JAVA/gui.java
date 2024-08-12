import java.util.*;
import java.awt.*;
import java.awt.event.*;

public class gui extends Frame{
    Label myLabel;
    /**
     * 
     */
    void MyFrame(){
        setSize(400,200);
        setTitle("my application");
        setVisible(true);
        myLabel=new Label("this is a label");
        add(myLabel);
        addWindowListener(new WindowAdapter(){
            public void windowClosing(final WindoEvent we)
            {
                System.exit(0);
            }
        });
    }
    public static void main(String[] s){
        Myframe=new MyFrame();
    }

}