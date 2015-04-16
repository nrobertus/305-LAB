#lang racket
; type in (f '(3 1 4 1 5 9))
(define (f lst)
  (display lst)
  (newline)
  ; (a) ;
  (if (null? lst)
      ; (b) ;
      '()
  ; (c) ;
  (cons (+ 1 (car lst)) (f (cdr lst)))))

; type in (member? 4 '(3 1 4 1 5 9))
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
; type in (set? '(3 1 4 1 5 9))
(define (set? lst)
  ; If - else ;
  (cond
    ; if list is null, return true ;
    ((null? lst) #t)
    ; check to see if the first element is repeated ;
    ((member? (car lst) (cdr lst)) #f)
    ; if first element isnt member, check cdr of list ;
    (else (set? (cdr lst))))
)

; this will join list 1 and list 2
(define (union lst1 lst2)
  (unionHelp '() (append lst1 lst2))
)

; this will make a set that holds the union of list 1 and list 2
(define (unionHelp lst1 lst2)
  (cond
    ; if list is null, return the completed list ;
    ((null? lst2) lst1)
    ; check to see if element repeated and remove if it is ;
    ((member? (car lst2) (cdr lst2)) (unionHelp lst1 (cdr lst2)))
    ; add the non repeated element to the set ;
    (else (unionHelp (append lst1 (list (car lst2))) (cdr lst2))))
)

; this will join list 1 and list 2
(define (intersect lst1 lst2)
  (intersectHelp '() (append lst1 lst2))
)

;this will make a set that holds the intersection of list 1 and list 2
(define (intersectHelp lst1 lst2)
  (cond
    ; if list is null, return the completed list ;
    ((null? lst2) lst1)
    ; check to see if element repeated and remove if it is ;
    ((member? (car lst2) (cdr lst2)) (intersectHelp (append lst1(list (car lst2))) (cdr lst2)))
    ; add the non repeated element to the set ;
    (else (intersectHelp lst1 (cdr lst2))))
)

(f '(3 1 4 1 5 9))
(member? 'one '(1 2 3 4))
(set? '(it was the best of times, it was the worst of times))
(union '(green eggs and) '(ham))
(intersect '(stewed tomatoes and macaroni) '(macaroni and cheese))
(intersect '(2 3 5 6 8 9) '(1 2 4 5 7 8))