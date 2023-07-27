import { Component, Input, OnInit } from '@angular/core';
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
export class ReviewComponent implements OnInit{
  DATA: Review[] = []
  constructor(private backendService: BackendCommunicationService) {}
  ngOnInit() {
    if (localStorage.getItem(this.movieTitle!+'-reviews')) {
      this.DATA = JSON.parse(localStorage.getItem(this.movieTitle!+'-reviews')!);
    } else {
      const num = Math.floor(Math.random() * 5);
      const sample_comments = [
        'This movie is great!',
        'This movie is good!',
        'This movie is ok!',
        'The plot is confusing',
        'This movie is bad!'
      ].reverse()
      for (let i = 0; i < num; i++) {
        const rating = Math.floor(Math.random() * 5) + 1;
        this.DATA.push({
          username: 'user' + i,
          comment: sample_comments[rating - 1],
          rating: rating
      });
    }
      localStorage.setItem(this.movieTitle!+'-reviews', JSON.stringify(this.DATA));
    }
    
  }

  username: string = localStorage.getItem('username')!;

  @Input() movieTitle: string = '';

  ngOnChanges(changes: SimpleChanges, force=false) {
    if (changes['movieTitle'] || force) {
      console.log('movieTitle changed from Review: ', this.movieTitle);
      // fetch comments for that move and update DATA

      // this.backendService.getMovieReviews(this.movieTitle).subscribe(
      //   (value: any) => {
      //     
      //     value = value as Review[]
      //     this.DATA = value;
      //   }
      // )

      if (localStorage.getItem(this.movieTitle!+'-reviews')) {
        this.DATA = JSON.parse(localStorage.getItem(this.movieTitle!+'-reviews')!);
      } else {
        const num = Math.floor(Math.random() * 5);
        const sample_comments = [
          'I thoroughly enjoyed this movie. The plot was engaging, the performances were outstanding, and it had a perfect balance of humor and emotion.',
          'This movie had a perfect blend of humor and heart. It made me laugh out loud one moment and brought tears to my eyes the next, creating a truly emotional and enjoyable experience.',
          'The attention to detail in the costume design of this movie was impeccable. The costumes not only captured the essence of the characters but also added to the overall visual aesthetic.',
          'I was disappointed by this movie. The story felt cliché, and the characters were poorly developed. It didn\'t offer anything new or memorable.',
          'I was disappointed by this movie. The story felt cliché, and the characters were poorly developed. It didn\'t offer anything new or memorable.'
        ].reverse()
        for (let i = 0; i < num; i++) {
          const rating = Math.floor(Math.random() * 5) + 1;
          this.DATA.push({
            username: 'user' + i,
            comment: sample_comments[rating - 1],
            rating: rating
        });
      }
        localStorage.setItem(this.movieTitle!+'-reviews', JSON.stringify(this.DATA));
      }

    }
  }

  newReview: Review = {
    username: localStorage.getItem('username')!,
    comment: '',
    rating: 3
  }

  addReview(): void {
    // this.backendService.addReview(this.newReview.username, this.movieTitle, this.newReview.rating, this.newReview.comment).subscribe(res => {
    //   // Refresh the reviews after adding
    //   this.ngOnChanges({}, true);
    // });
    this.DATA.push(this.newReview);
    localStorage.setItem(this.movieTitle!+'-reviews', JSON.stringify(this.DATA));

  }

  editReview(): void {
    this.backendService.editReview(this.newReview.username, this.movieTitle, this.newReview.rating, this.newReview.comment).subscribe(res => {
      // Refresh the reviews after editing
      this.ngOnChanges({}, true);
    });
  }

  deleteReview(): void {
    // this.backendService.deleteReview(localStorage.getItem('username')!, this.movieTitle).subscribe(res => {
    //   // Refresh the reviews after deleting
    //   this.ngOnChanges({});
    // });
    this.DATA = this.DATA.filter(review => review.username !== this.username);
    localStorage.setItem(this.movieTitle!+'-reviews', JSON.stringify(this.DATA));
  }

}
