import { Component } from '@angular/core';

@Component({
  selector: 'app-recommendations',
  templateUrl: './recommendations.component.html',
  styleUrls: ['./recommendations.component.scss']
})
export class RecommendationsComponent {
  RecommendationList: string[] = ['The Dark Knight', 'The Godfather', '12 Angry Men', 'The Shawshank Redemption', "Schindler's List"]
  
}
