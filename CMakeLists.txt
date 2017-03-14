cmake_minimum_required(VERSION 3.6)
project(cython_opencv_stuff)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES main.cpp)
add_executable(cython_opencv_stuff ${SOURCE_FILES})