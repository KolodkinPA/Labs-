cmake_minimum_required(VERSION 3.6)
project(laba4)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=c90")

set(SOURCE_FILES main.c)
add_executable(laba4 ${SOURCE_FILES})
target_link_libraries(laba4 m)