cmake_minimum_required(VERSION 3.6)
project(untitled1)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -lm -std=c90")

set(SOURCE_FILES main.c)
add_executable(untitled1 ${SOURCE_FILES})
target_link_libraries(untitled1 m)