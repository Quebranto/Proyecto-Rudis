cmake_minimum_required(VERSION 3.16)
project(RudisConversionPalace LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_library(RudisConversionPalace ConversionPalace.cpp)
target_include_directories(RudisConversionPalace PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

add_executable(RudisConversionPalaceTest ConversionPalace.test.cpp)
target_link_libraries(RudisConversionPalaceTest PRIVATE RudisConversionPalace)

enable_testing()
add_test(NAME RudisConversionPalaceTest COMMAND RudisConversionPalaceTest)
