#include <cstdio>
#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

using namespace std::chrono_literals;

int main(int argc, char ** argv)
{
  (void) argc;
  (void) argv;

  printf("hello world test_image package\n");
  return 0;
}
