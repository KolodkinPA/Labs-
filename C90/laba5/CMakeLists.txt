cmake_minimum_required(VERSION 3.6)
project(laba5)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=c90")

set(SOURCE_FILES main.c)
add_executable(laba5 ${SOURCE_FILES})
target_link_libraries(laba5 m)