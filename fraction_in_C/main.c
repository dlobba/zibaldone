#include "fraction.h"
#include <stdio.h>
#include <stdlib.h>

int
main ()
{
  Fraction fract1 = {.numerator = -1, .denominator = -2};
  Fraction fract2 = {.numerator = 1, .denominator = 4};

  int a = lcm (-3, -4);
  Fraction b = fraction_sum (&fract1, &fract2);

  printf ("%d/%d\n", b.numerator, b.denominator);


  b = fraction_negate (&fract1);
  
  char *tmp = fraction_to_string (&b);
  
  printf ("%s\n", tmp);

  b = fraction_difference (&fract1, &fract2);
  
  tmp = fraction_to_string (&b);
  printf ("%s\n", tmp);
  
  free(tmp);

  Fraction f = {.numerator = 13, .denominator = 18};
  f = fraction_multiply (&f, &fract1);

  f = fraction_multiply_by_scalar (&f, 2);

  f = fraction_divide (&f, &f);
  
  printf ("Test: %d/%d", f.numerator, f.denominator);
  
  return 0;
}
