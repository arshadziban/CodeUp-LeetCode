class Person {
    String name;
    int age;

    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
}

class Student extends Person {
    int studentId;
    char grade;

    Student(String name, int age, int studentId, char grade) {
        super(name, age);
        this.studentId = studentId;
        this.grade = grade;
    }

    void display() {
        System.out.println("Student Information");
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Student ID: " + studentId);
        System.out.println("Grade: " + grade);
    
    }
}

public class StudentProgram {
    public static void main(String[] args) {
    Student student1 = new Student("John Doe", 20, 10125, 'A');
        student1.display();
    }
}
