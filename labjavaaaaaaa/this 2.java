class Pen{
    String color;
    public void write(){
        System.out.println("Writeing things");
    }
    public void color(){
     System.out.println(this.color);
    }
    
}
public class OOPS{
    public static void main(String[] args){
        Pen pen1 = new Pen();
        pen1.color= "blue";
        pen1.write();
        pen1.color();
    }
}
