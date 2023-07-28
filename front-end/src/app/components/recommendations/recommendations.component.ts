import { Component, OnInit } from '@angular/core';
import { BackendCommunicationService } from 'src/app/services/backend-communication.service';
import { MovieService } from 'src/app/services/movie.service';

export interface RecommendationSlide {
  title: string;
  src: string;
}

@Component({
  selector: 'app-recommendations',
  templateUrl: './recommendations.component.html',
  styleUrls: ['./recommendations.component.scss'],
})
export class RecommendationsComponent implements OnInit {
  index = 0;
  forward() {
    this.index = (this.index + 1) % this.recommendations.length;
    console.log('index: ', this.index);
  }
  backward() {
    this.index =
      (this.index - 1 + this.recommendations.length) %
      this.recommendations.length;
    console.log('index: ', this.index);
  }

  removeSuggestion() {
    alert('Removing index: ' + this.index);
    this.recommendationMovieNames[this.index] = "Barbie"
    this.loadMovieRecommendations();
  }
  constructor(private movieSerivce: MovieService,
    private backendService: BackendCommunicationService) {}

  doneLoading: boolean = false;

  recommendationMovieNames: string[] = [];

  recommendations: RecommendationSlide[] = [];

  async loadMovieRecommendations() {
    this.doneLoading = false;
    const movieSrcs: Promise<string>[] = this.recommendationMovieNames.map(
      async (movie) => {
        return await this.movieSerivce.getMovieImage(movie);
      }
    );

    const resolvedMovieSrcs = await Promise.all(movieSrcs);

    this.recommendations = this.recommendationMovieNames.map((movie, i) => {
      return {
        title: movie,
        src: resolvedMovieSrcs[i],
      } as RecommendationSlide;
    });

    console.log(this.recommendations);
    this.doneLoading = true;
  }

  ngOnInit() {
    this.backendService.getRecommendedMovies(sessionStorage.getItem('username')!).subscribe(
      (data: any) => {
        alert("User recommendations from backend: "+JSON.stringify(data))
        this.recommendationMovieNames = data as string[];
        this.loadMovieRecommendations();
      }
    )
  }
  
}
