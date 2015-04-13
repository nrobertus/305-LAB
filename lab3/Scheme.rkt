#lang racket
(define (f lst)
  (display lst)
  (newline)
  ; (a) ;
  (if (null? lst)
      ; (b) ;
      '()
  ; (c) ;
  (cons (+ 1 (car lst)) (f (cdr lst)))))

(define (member? e lst)
  ; This is basically an else if statement ;
  (cond
    ; if the list is null, return false ;
    ((null? lst) #f)
    ; if e is equal to the first element in the list, return true;
    ((eq? e (car lst)) #t)
    ; if e is not equal to the first element in the list, return the recursive call of
    ; everything after the first element of the lsit ;
    (else (member? e (cdr lst))))
)