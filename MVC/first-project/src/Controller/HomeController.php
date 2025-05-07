<?php

namespace App\Controller;

use App\Service\LoremService;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

final class HomeController extends AbstractController
{
    #[Route('/', name: 'app_home')]
    public function index(LoremService $loremService): Response
    {
        return $this->render('home/index.html.twig', [
            'controller_name' => $loremService->getMyName(),
        ]);
    }
}
