package com.example.movierentalreviewsystemcs348.jdbc;

public class Things {
    private Long id;
    private String name;
    public Things(){}
    public Things(long id, String name){
        this.id = id;
    }

    @Override
    public String toString() {
        return "Things{" +
                "id=" + id +
                ", name='" + name + '\'' +
                '}';
    }
}
