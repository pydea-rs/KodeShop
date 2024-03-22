import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HeaderComponent } from './sections/header/header.component';
import { FooterComponent } from './sections/footer/footer.component';
import { AuthModalsComponent } from './sections/auth-modals/auth-modals.component';
import { NavBarComponent } from './sections/nav-bar/nav-bar.component';
import { HomePageComponent } from './pages/home-page/home-page.component';
import { LatestNewsComponent } from './sections/latest-news/latest-news.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, HeaderComponent, FooterComponent, AuthModalsComponent, NavBarComponent, HomePageComponent, LatestNewsComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'ng-template';
}
