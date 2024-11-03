class Empolyee{
    int money;
    String name;
    public int getmoney(){
        return money;
    }
    public String getname(){
        return name;
    }
    public void setname(String abhi){
        name =abhi;
    }
}
public class Job{
    public static void main(String[] args){
        Empolyee emp = new Empolyee();
        emp.setname("modigiii");
        System.out.println(emp.getname());
       emp.money=2000;
       System.out.println(emp.getmoney());
    }
}
