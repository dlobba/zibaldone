#ifndef FRACTION_H
#define FRACTION_H

typedef struct _Fraction {
  int numerator;
  int denominator;
} Fraction;

Fraction fraction_negate (const Fraction*);
Fraction fraction_sum (const Fraction*, const Fraction*);
Fraction fraction_difference (const Fraction*, const Fraction*);
Fraction fraction_multiply (const Fraction*, const Fraction*);
Fraction fraction_multiply_by_scalar (const Fraction*, const int);
Fraction fraction_divide (const Fraction*, const Fraction*);
Fraction fraction_simplify (const Fraction*);


int gcd (int, int);
int lcm (int, int);

char* fraction_to_string (const Fraction*);

#endif
