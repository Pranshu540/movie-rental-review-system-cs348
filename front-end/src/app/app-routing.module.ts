import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './components/login/login.component'
import { HomeComponent } from './components/home/home.component';
import { SearchComponent } from './components/search/search.component';
import { MovieComponent } from './components/movie/movie.component';
import { AuthGuard } from './auth.guard';
import { HeaderComponent } from './components/header/header.component';
import { RentalViewComponent } from './components/rental-view/rental-view.component';

const routes: Routes = [
  { path: 'login', component : LoginComponent},
  { path: '', redirectTo: '/login', pathMatch: 'full' },
  { path: 'home', component: SearchComponent, canActivate: [AuthGuard] },
  { path: 'header', component: HeaderComponent},
  {path: 'rentals', component: RentalViewComponent}
  // { path: 'movies/:name', component: MovieComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
  

}
