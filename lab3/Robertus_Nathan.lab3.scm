#lang racket
(define (f lst)
  (display lst)
  (newline)
  ; (a) ;
  (if (null? lst) ; if the list is null
      ; (b) ;
      '() ; return nothing
  ; (c) ;
  (cons (+ 1 (car lst)) (f (cdr lst))))) ; else return everything but the first element recursively.

(define (member? e lst)
  (cond
    ((null? lst) #f); if the list is null, return false ;
    ((eq? e (car lst)) #t); if e is equal to the first element in the list, return true;
    (else (member? e (cdr lst)))); if e is not equal to the first element in the list, call member on everything else.
)

(define (set? lst)
  (cond ; if list is null, return true ;
    ((null? lst) #t)
    ((member? (car lst) (cdr lst)) #f) ; check to see if the first element is repeated ;
    (else (set? (cdr lst)))); if first element isnt member, check cdr of list ;
)

(define (union lst1 lst2) ; this will join list 1 and list 2
  (unionHelp '() (append lst1 lst2))
)

(define (unionHelp lst1 lst2) ; this will make a set that holds the union of list 1 and list 2
  (cond
    ((null? lst2) lst1) ; if list is null, return the completed list ;
    ((member? (car lst2) (cdr lst2)) (unionHelp lst1 (cdr lst2))) ; check to see if element repeated and remove if it is ;
    (else (unionHelp (append lst1 (list (car lst2))) (cdr lst2)))) ; add the non repeated element to the set ;
)


(define (intersect lst1 lst2) ; this will join list 1 and list 2
  (intersectHelp '() (append lst1 lst2))
)


(define (intersectHelp lst1 lst2) ; this will make a set that holds the intersection of list 1 and list 2
  (cond
    ((null? lst2) lst1) ; if list is null, return the completed list ;
    ((member? (car lst2) (cdr lst2)) (intersectHelp (append lst1(list (car lst2))) (cdr lst2))); check to see if element repeated and remove if it is ;
    (else (intersectHelp lst1 (cdr lst2)))); add the non repeated element to the set ;
)


(define (flattenSingle x) ; this is the helper function that flattens a single list.
    (cond ((null? x) '()) ; if the list is empty, return it
          ((not (pair? x)) (list x)) ; if there is only one element, return it in list form
          (else (append (flattenSingle (car x)) ; append the flattened head onto the flattened tail
                        (flattenSingle (cdr x))))))

(define (flatten lst1 lst2) ; this function just takes the union of two lists that are flattened by the helper function.
  (union (flattenSingle lst1) (flattenSingle lst2)) ; take the union of the two flattened lists
)

(f '(3 1 4 1 5 9))
(member? 'one '(1 2 3 4))
(set? '(it was the best of times, it was the worst of times))
(union '(green eggs and) '(ham))
(intersect '(stewed tomatoes and macaroni) '(macaroni and cheese))
(intersect '(2 3 5 6 8 9) '(1 2 4 5 7 8))
(flatten '(1 (2 3) 5) '(8 (13 (21 34) 55)))