#include "fraction.h"
#include <stdio.h>
#include <stdlib.h>

int
gcd (int num1,
     int num2)
{
  int tmp;
  while (num2 != 0) {
    tmp = num2;
    num2 = num1 % num2;
    num1 = tmp;
  }

  return num1; 
}

int
lcm (int num1,
     int num2)
{
  int lcm = num1 / gcd (num1, num2) *  num2;
  return lcm;
}

Fraction
fraction_negate (const Fraction* fraction)
{
  Fraction result = {
    .numerator = -fraction->numerator,
    .denominator = fraction->denominator
  };
  return result;
}

Fraction
fraction_sum (const Fraction *fract1,
	      const Fraction *fract2)
{

  int denominator = lcm (fract1->denominator, fract2->denominator);
  int numerator = denominator / fract1->denominator * fract1->numerator +
    denominator / fract2->denominator * fract2->numerator;
  
  Fraction result = {.numerator = numerator, .denominator = denominator};
  return fraction_simplify (&result);
  
}


Fraction
fraction_difference (const Fraction* fract1,
		     const Fraction* fract2)
{
  Fraction tmp = fraction_negate (fract2);
  return fraction_sum (fract1, &tmp);

}


Fraction
fraction_simplify (const Fraction* fract)
{

  int s = gcd (fract->numerator, fract->denominator);
  Fraction tmp = {.numerator = fract->numerator / s,
		  .denominator = fract->denominator / s};

  return tmp;	  
  
}

Fraction
fraction_multiply (const Fraction* fract1,
		   const Fraction* fract2)
{
  Fraction result;
  result.numerator = fract1->numerator * fract2->numerator;
  result.denominator = fract1->denominator * fract2-> denominator;

  return fraction_simplify (&result);
}


Fraction
fraction_multiply_by_scalar (const Fraction* fraction,
			     const int scalar)
{

  Fraction result = {.numerator = fraction->numerator * scalar, .denominator = fraction->denominator};
  return fraction_simplify (&result);
  
}


Fraction
fraction_divide (const Fraction* fract1,
		 const Fraction* fract2)
{
  Fraction tmp = {.numerator = fract2->denominator,
  .denominator = fract2->numerator};
  
  return fraction_multiply (fract1, &tmp);
}


char*
fraction_to_string
(const Fraction* fraction)
{
  if (fraction->numerator == fraction->denominator)
    return "1";
  
  int char_required = snprintf (NULL, 0, "%d/%d", fraction->numerator, fraction->denominator) + 1;

  char *tmp_string = malloc (sizeof (char) * char_required);

  snprintf (tmp_string, char_required, "%d/%d", fraction->numerator, fraction->denominator);

  return tmp_string;
  
}
