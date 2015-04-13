#lang racket
(define (f lst)
  ; (a) This line checks to see if the list is null ;
  (if (null? lst)
      ; (b)This line creates a new list for the modified numbers to be put into ;
      '()
      ; (c)This line adds one to the first element in the list and recursively removes the first 
      ;element from the list and calls f again. ;
      (cons (+ 1 (car lst)) (f (cdr lst)))))