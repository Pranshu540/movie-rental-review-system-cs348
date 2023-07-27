import { Component, Input } from '@angular/core';
import { SimpleChanges } from '@angular/core';


export interface Review {
  username: string,
  comment: string,
  rating: number // between 1 and 5
}



@Component({
  selector: 'app-review',
  templateUrl: './review.component.html',
  styleUrls: ['./review.component.scss']
})
export class ReviewComponent {
  DATA: Review[] = [
    {username: "MovieBoi", comment: "This movie sux", rating: 1},
    {username: "FlixBoi", comment: "This movie is good. MovieBoi doesn't understand good movies.", rating: 3}
  ]

  @Input() movieTitle: string = '';

  ngOnChanges(changes: SimpleChanges) {
    if (changes['movieTitle']) {
      console.log('movieTitle changed from Review: ', this.movieTitle);
      // fetch comments for that move and update DATA
    }
  }

}
