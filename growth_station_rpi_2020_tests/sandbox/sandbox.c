#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#ifndef PI
  #define PI 3.14159265
#endif

int main()
{
  double tstamp = (double)time(NULL);
  srand(tstamp);
  double initialOffset = rand() % 100; // Make this random?
  printf("Initial offset: %f\n", initialOffset);
  double mean = 7.1;
  double deviation = 0.5;
  //printf("Timestamp: %f\n", tstamp);
  double result = sin((initialOffset + tstamp)*PI/180);
  double finalValue = mean + (deviation * result);
  printf("Final value: %f\n", finalValue);
  return 0;
}

void getMinMax()
{
  double min, max;
  double result;

  for (double input = 0; input < 500; input++)
  {
    result = sin(input*PI/180);
    if ( input == 0 )
    {
      min = result;
      max = result;
    }
    else if ( min > result )
    {
      min = result;
    }
    else if ( max < result )
    {
      max = result;
    }
  }

  printf("Range: %f, %f\n", min, max);
}
