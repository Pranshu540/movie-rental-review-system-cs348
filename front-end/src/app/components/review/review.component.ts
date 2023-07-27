import { Component, Input } from '@angular/core';
import { SimpleChanges } from '@angular/core';
import { BackendCommunicationService } from 'src/app/services/backend-communication.service';


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
  constructor(private backendService: BackendCommunicationService) {}
  DATA: Review[] = [
    {username: "MovieBoi", comment: "This movie sux", rating: 1},
    {username: "nj", comment: "This movie is good. MovieBoi doesn't understand good movies.", rating: 3}
  ]

  username: string = sessionStorage.getItem('username')!;
  isAdmin: boolean = sessionStorage.getItem('isAdmin') === 'true';

  @Input() movieTitle: string = '';

  ngOnChanges(changes: SimpleChanges, force=false) {
    if (changes['movieTitle'] || force) {
      console.log('movieTitle changed from Review: ', this.movieTitle);
      // fetch comments for that move and update DATA

      this.backendService.getMovieReviews(this.movieTitle).subscribe(
        (value: any) => {
          alert("reviews from backend: "+JSON.stringify(value))
          value = value as Review[]
          this.DATA = value;
        }
      )

    }
  }

  newReview: Review = {
    username: sessionStorage.getItem('username')!,
    comment: '',
    rating: 3
  }

  addReview(): void {
    this.backendService.addReview(this.newReview.username, this.movieTitle, this.newReview.rating, this.newReview.comment).subscribe(res => {
      // Refresh the reviews after adding
      this.ngOnChanges({}, true);
    });

  }

  editReview(): void {
    this.backendService.editReview(this.newReview.username, this.movieTitle, this.newReview.rating, this.newReview.comment).subscribe(res => {
      // Refresh the reviews after editing
      this.ngOnChanges({}, true);
    });
  }

  deleteReview(): void {
    this.backendService.deleteReview(sessionStorage.getItem('username')!, this.movieTitle).subscribe(res => {
      // Refresh the reviews after deleting
      this.ngOnChanges({});
    });
  }

}
