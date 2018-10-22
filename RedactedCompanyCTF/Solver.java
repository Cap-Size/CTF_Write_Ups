import java.awt.Color;
import javax.swing.JButton;
import java.awt.Font;

public class L{
    public static JButton b = new JButton("CHECK PASSWORD");
  
    public static String twist(String a) {
        char[] b = a.toCharArray();
        for (int i = 0; i < b.length - 2; i++) {
            char temp = b[i];
            b[i] = b[(i + 2)];
            b[(i + 2)] = temp;   
        }
        String c = new String(b);
        return c;
    }

  public static String getKey(){
    b.setFont(new Font("Times New Roman", 1, 50));
    String B = "Z";
    String key = "";
    key = key + (char)(Color.DARK_GRAY.getGreen() + 13);
    key = key + 7;
    key = key + 3;
    String w39 = "";
    key = key + "Flag";
    key = key.replace("" + key.charAt(3), "_");
    
    String k = "";
    int i = key.length();
    while (i-- > 0) {
      w39 = "Qb7";
      k = k + key.charAt(i);
    }
    key = k;
    key = key + w39;
    key.replace("Q", "uhoh");
    key = key + b.getFont().getName().charAt(0);
    
    key = twist(key);
    
    key = key + B;
    
    return key;
  }
  public static void main(String[] args) {
    String a = getKey();
    System.out.println(a);
  }
}