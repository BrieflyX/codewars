/*
    Write a program that will calculate the number of trailing zeros in a factorial of a given number.

    N! = 1 * 2 * 3 * 4 ... N

    zeros(12) = 2 # 1 * 2 * 3 .. 12 = 479001600 
    that has 2 trailing zeros 4790016(00)
    Be careful 1000! has length of 2568 digital numbers.
*/

// my code, last point exceed 6000ms time
function zeros (n) {
    var fac2 = 0, fac5 = 0, fac10 = 0;
    for (i=1;i<=n;i++){
        var j=i;
        while (j%10==0){fac10++;j/=10;}
        while (j%2==0) {fac2++;j/=2;}
        while (j%5==0) {fac5++;j/=5;}
    }
    if (fac2 > fac5)  return fac5+fac10
    else              return fac2+fac10
}

// other code
function zeros_others (n) {
  var zs = 0;
  while(n>0){
    n=Math.floor(n/5);
    zs+=n
  }
  return zs;
}

/*
    depends on that method
    set f(n) to represent the number of tariling zeros in n!
    when 0 < n < 5, f(n!) = 0;
    when n >= 5, f(n!) = k + f(k!), k = Math.floor(n/5)
*/