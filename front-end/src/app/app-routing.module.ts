import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './components/login/login.component'
import { HomeComponent } from './components/home/home.component';
import { SearchComponent } from './components/search/search.component';
import { MovieComponent } from './components/movie/movie.component';
import { AuthGuard } from './auth.guard';

const routes: Routes = [
  { path: 'login', component : LoginComponent},
  { path: '', redirectTo: '/login', pathMatch: 'full' },
  { path: 'home', component: SearchComponent, canActivate: [AuthGuard] },
  // { path: 'movies/:name', component: MovieComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
  

}
